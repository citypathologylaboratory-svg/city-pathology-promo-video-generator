"""
City Pathology Laboratory - Promotional Video Generator
A Streamlit app to generate 15-second promotional videos with mascot image, script, and background music.
"""

import streamlit as st
import os
from pathlib import Path
from PIL import Image
import cv2
import numpy as np
from moviepy.editor import ImageClip, CompositeVideoClip, TextClip, AudioFileClip, concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import tempfile
import time

# Try to import TTS libraries
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

# Brand Colors
BRAND_BLUE = (0, 86, 179)  # RGB for #0056b3
BRAND_WHITE = (255, 255, 255)
VIDEO_DURATION = 15  # 15 seconds
FPS = 24
RESOLUTION = (1080, 1920)  # 9:16 aspect ratio for Instagram/WhatsApp Reels

# Page Configuration
st.set_page_config(
    page_title="City Path Lab - Promo Video Creator",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for branding
st.markdown("""
<style>
.stApp {
    background-color: #f5f5f5;
}
.stTitle {
    color: #0056b3;
    text-align: center;
}
.header-banner {
    background: linear-gradient(135deg, #0056b3 0%, #004085 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown('<div class="header-banner"><h1>💬 City Path Lab - Promo Video Creator</h1><p>Create engaging 15-second promotional videos for social media</p></div>', unsafe_allow_html=True)

# Main Layout
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("📄 Script & Configuration")
    
    # Test Type Selection
    test_type = st.selectbox(
        "Select Test Type",
        ["Thyroid", "FNAC", "CBC", "Lipid Profile", "COVID-19", "Other"]
    )
    
    # Language Selection
    language = st.selectbox(
        "Select Language",
        ["English", "Gujarati", "Hindi"]
    )
    
    # Script Text Area
    script = st.text_area(
        "Enter Your Script",
        value="Get your tests done today!",
        height=150,
        help="Enter the promotional message (max 200 characters for 15 seconds)"
    )
    
    if len(script) > 200:
        st.warning("⚠️ Script is too long. Please keep it under 200 characters for a 15-second video.")
    
    # Audio Selection
    audio_type = st.radio(
        "Select Background Music Style",
        ["Energetic", "Calm"],
        help="Choose the mood for your video (Currently using placeholder audio)"
    )

with col2:
    st.subheader("🖼 Mascot Image")
    
    # File Uploader for Mascot
    uploaded_file = st.file_uploader(
        "Upload Mascot Image",
        type=["jpg", "jpeg", "png", "gif"],
        help="Upload a PNG, JPG, or GIF image of your mascot"
    )
    
    if uploaded_file:
        # Display uploaded image preview
        image = Image.open(uploaded_file)
        st.image(image, caption="Mascot Preview", use_column_width=True)
        st.success("✅ Image uploaded successfully!")
    else:
        st.info("Please upload a mascot image to proceed")

# Advanced Settings
with st.expander("⚙️ Advanced Settings"):
    text_color = st.color_picker("Text Color", value="#FFFFFF", help="Color for the script text")
    bg_color = st.color_picker("Text Background Color", value="#0056b3", help="Background color for text overlay")
    font_size = st.slider("Font Size", 20, 60, 40, help="Size of the text overlay")
    animation_type = st.selectbox(
        "Mascot Animation",
        ["Zoom In", "Slide In", "Pulse", "Bounce"],
        help="Choose animation effect for the mascot"
    )

def apply_lip_sync_ai(mascot_frame, audio_duration, animation_frame):
    """
    Placeholder function for AI lip-sync animation.
    This function can later be integrated with APIs like D-ID or SadTalker.
    
    Current implementation:
    - Applies a subtle pulse/scale effect to simulate mouth movement
    - Can be extended with actual lip-sync AI in the future
    
    Args:
        mascot_frame: The mascot image as numpy array
        audio_duration: Duration of the audio in seconds
        animation_frame: Current frame number
    
    Returns:
        Modified mascot frame with animation effect
    """
    
    # Simple pulse effect using sine wave
    # Scale factor varies between 0.95 and 1.05 to simulate talking
    pulse_frequency = 3  # Hz (3 pulses per second)
    time_value = (animation_frame / FPS) * (2 * np.pi * pulse_frequency)
    scale_factor = 1.0 + 0.05 * np.sin(time_value)  # Varies between 0.95 and 1.05
    
    # This is a placeholder for future integration
    # TODO: Integrate with D-ID or SadTalker API for actual lip-sync
    
    return mascot_frame, scale_factor

def create_video(mascot_image, script_text, language, audio_type, animation_type):
    """
    Create a promotional video with mascot, script, and audio.
    
    Args:
        mascot_image: PIL Image object of the mascot
        script_text: Text string for the script
        language: Selected language (English, Gujarati, Hindi)
        audio_type: Audio style (Energetic or Calm)
        animation_type: Type of animation effect
    
    Returns:
        Path to the generated video file
    """
    
    try:
        # Create temporary directory for intermediate files
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Step 1: Save mascot image
            mascot_path = temp_path / "mascot.png"
            mascot_image.save(mascot_path)
            
            # Step 2: Generate audio using gTTS
            audio_path = temp_path / "audio.mp3"
            
            if GTTS_AVAILABLE:
                tts_lang_map = {
                    "English": "en",
                    "Gujarati": "gu",
                    "Hindi": "hi"
                }
                tts = gTTS(text=script_text, lang=tts_lang_map.get(language, "en"), slow=False)
                tts.save(audio_path)
            else:
                st.warning("퉪 Generating placeholder audio (gTTS not installed)")
                # For now, we'll use a placeholder - in production, ensure gTTS is installed
                return None
            
            # Step 3: Create video clips
            # Load mascot image and create image clip
            mascot_clip = ImageClip(str(mascot_path)).set_duration(VIDEO_DURATION)
            
            # Load audio
            audio_clip = AudioFileClip(str(audio_path))
            audio_duration = min(audio_clip.duration, VIDEO_DURATION)
            
            # Resize mascot to fit resolution (center it)
            mascot_width = int(RESOLUTION[0] * 0.6)
            mascot_clip = mascot_clip.resize(width=mascot_width)
            
            # Position mascot in center
            mascot_clip = mascot_clip.set_position('center')
            
            # Step 4: Create header text ("City Pathology Laboratory")
            header_clip = TextClip(
                "City Pathology Laboratory",
                fontsize=45,
                color='white',
                font='Arial-Bold',
                method='caption',
                size=(RESOLUTION[0]-40, None),
                bg_color='#0056b3'
            ).set_duration(VIDEO_DURATION).set_position(('center', 50))
            
            # Step 5: Create script text overlay
            script_clip = TextClip(
                script_text,
                fontsize=font_size,
                color=text_color.lstrip('#'),
                font='Arial',
                method='caption',
                size=(RESOLUTION[0]-60, 200),
                bg_color=bg_color.lstrip('#')
            ).set_duration(audio_duration).set_position(('center', RESOLUTION[1]-300))
            
            # Step 6: Composite video
            final_video = CompositeVideoClip(
                [ImageClip(np.zeros((RESOLUTION[1], RESOLUTION[0], 3)), duration=VIDEO_DURATION).set_color("white"),
                 mascot_clip,
                 header_clip,
                 script_clip],
                size=RESOLUTION
            ).set_audio(audio_clip.subclipped(0, min(audio_duration, VIDEO_DURATION)))
            
            # Step 7: Write video file
            output_path = temp_path / "promo_video.mp4"
            final_video.write_videofile(
                str(output_path),
                fps=FPS,
                codec='libx264',
                audio_codec='aac',
                verbose=False,
                logger=None
            )
            
            return output_path
    
    except Exception as e:
        st.error(f"⚠️ Error creating video: {str(e)}")
        return None

# Generate Button and Output
st.markdown("---")
col_generate, col_download = st.columns(2)

with col_generate:
    if st.button("🎞️ Generate Video", use_container_width=True, type="primary"):
        if not uploaded_file:
            st.error("⚠️ Please upload a mascot image first!")
        elif not script.strip():
            st.error("⚠️ Please enter a script!")
        else:
            with st.spinner("🎞Generating your promotional video..."):
                image = Image.open(uploaded_file)
                video_path = create_video(
                    image,
                    script,
                    language,
                    audio_type,
                    animation_type
                )
                
                if video_path:
                    st.session_state.video_path = video_path
                    st.success("✅ Video generated successfully!")
                    # Display success message with video details
                    st.info(f"📊 Video Details:\n- Duration: {VIDEO_DURATION} seconds\n- Language: {language}\n- Test Type: {test_type}\n- Audio Style: {audio_type}")

# Download Video
if 'video_path' in st.session_state and st.session_state.video_path:
    with open(st.session_state.video_path, 'rb') as video_file:
        st.download_button(
            label="💥 Download Video",
            data=video_file.read(),
            file_name=f"city_path_promo_{test_type.lower()}.mp4",
            mime="video/mp4",
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px; margin-top: 30px;'>
<p>💬 <strong>City Pathology Laboratory - Promo Video Creator</strong></p>
<p>Create engaging promotional videos effortlessly | Supports Multiple Languages</p>
<p><em>For support or feedback, contact: support@citypathlab.in</em></p>
</div>
""", unsafe_allow_html=True)
