# city-pathology-promo-video-generator

## Overview

A powerful Streamlit-based web application designed for **City Pathology Laboratory** to generate engaging 15-second promotional videos for social media platforms (WhatsApp, Instagram Reels, etc.). The app combines mascot images, custom scripts, and background music with professional text-to-speech conversion.

### Key Features

✅ **Multi-Language Support** - Gujarati, Hindi, and English
✅ **Professional Video Generation** - 9:16 aspect ratio optimized for mobile/social media
✅ **Text-to-Speech Integration** - Automatic script-to-audio conversion using gTTS
✅ **Multiple Test Types** - Thyroid, FNAC, CBC, Lipid Profile, COVID-19, and more
✅ **Customizable Animations** - Zoom In, Slide In, Pulse, and Bounce effects
✅ **Brand Consistency** - Pre-configured brand colors (Blue #0056b3 & White)
✅ **Advanced Settings** - Fine-grained control over text color, size, and styling
✅ **AI Lip-Sync Ready** - Placeholder for D-ID or SadTalker API integration

---

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg (required by moviepy)
- pip (Python package manager)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/citypathologylaboratory-svg/city-pathology-promo-video-generator.git
cd city-pathology-promo-video-generator
```

#### 2. Install FFmpeg

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

#### 3. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Running the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Workflow

1. **Upload Mascot Image**
   - Click the "Upload Mascot Image" button
   - Select PNG, JPG, or GIF image of your laboratory mascot
   - Preview will display instantly

2. **Configure Video Settings**
   - Select Test Type (Thyroid, FNAC, CBC, etc.)
   - Choose Language (English, Gujarati, Hindi)
   - Enter Your Promotional Script (max 200 characters recommended)
   - Select Background Music Style (Energetic or Calm)

3. **Advanced Customization (Optional)**
   - Adjust Text Color and Background Color
   - Change Font Size
   - Select Animation Type

4. **Generate Video**
   - Click the "🎞️ Generate Video" button
   - Wait for processing (takes 30-60 seconds depending on script length)
   - Video will be generated with automatic text-to-speech

5. **Download**
   - Once generated, click "💥 Download Video" button
   - Video file will be saved as `city_path_promo_[testtype].mp4`

---

## Project Structure

```
city-pathology-promo-video-generator/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore file
```

---

## Core Components

### 1. User Interface (Streamlit)

- **Responsive Layout**: Two-column design for inputs and preview
- **Custom CSS**: Brand colors and professional styling
- **Real-time Validation**: Script length warnings and image preview
- **Advanced Settings**: Expandable menu for fine-tuning

### 2. Video Processing (moviepy)

- **Image Handling**: Resize and position mascot image
- **Text Overlays**: Header "City Pathology Laboratory" + Script text
- **Video Composition**: Combine images, text, and audio
- **Export**: MP4 format with H.264 codec

### 3. Audio Generation (gTTS)

- **Automatic Speech Synthesis**: Converts script text to MP3
- **Multi-Language**: Supports Hindi, Gujarati, and English
- **Natural Voice**: Google's text-to-speech engine

### 4. Lip-Sync Placeholder (apply_lip_sync_ai)

```python
def apply_lip_sync_ai(mascot_frame, audio_duration, animation_frame):
    """
    Placeholder for AI lip-sync animation.
    
    Future integration with:
    - D-ID API: Professional lip-sync
    - SadTalker: Advanced facial animation
    - Custom models: Fine-tuned for lab mascot
    """
```

---

## Configuration

### Video Settings

```python
VIDEO_DURATION = 15        # 15-second videos
FPS = 24                   # Frames per second
RESOLUTION = (1080, 1920)  # 9:16 aspect ratio (mobile-optimized)
```

### Brand Colors

```python
BRAND_BLUE = (0, 86, 179)    # #0056b3
BRAND_WHITE = (255, 255, 255)  # #FFFFFF
```

---

## Dependencies Explained

| Package | Version | Purpose |
|---------|---------|----------|
| streamlit | 1.28.0 | Web UI framework |
| moviepy | 1.0.3 | Video processing and composition |
| opencv-python | 4.8.1.78 | Image processing |
| Pillow | 10.0.0 | Image manipulation |
| gTTS | 2.3.2 | Text-to-speech conversion |
| numpy | 1.24.3 | Numerical operations |
| scipy | 1.11.2 | Scientific computing |
| pydub | 0.25.1 | Audio processing |

---

## Advanced: Integrating Lip-Sync AI

### Option 1: D-ID API

```python
# Future integration example
import requests

def apply_lip_sync_ai_did(mascot_image_path, script_text):
    # D-ID API integration
    # Replace placeholder with actual API calls
    pass
```

### Option 2: SadTalker

```python
# Local SadTalker integration
from sad_talker import SadTalkerAnimator

def apply_lip_sync_ai_sadtalker(mascot_image, audio_path):
    # SadTalker setup and execution
    pass
```

---

## Troubleshooting

### Issue: "FFmpeg not found"

**Solution:** Install FFmpeg and ensure it's in your system PATH.

### Issue: "gTTS not available"

**Solution:** Install gTTS: `pip install gtts`

### Issue: Video generation is slow

**Solution:** This is normal for 15-second videos. Optimize by:
- Shortening the script
- Reducing font size slightly
- Simplifying animation effects

### Issue: Text not rendering correctly

**Solution:** Ensure proper Unicode support for Gujarati/Hindi text.

---

## Performance Tips

1. **Script Length**: Keep scripts under 150 characters for optimal pacing
2. **Image Format**: Use PNG for transparency, JPG for smaller file sizes
3. **Font Size**: 30-45px recommended for 1080x1920 resolution
4. **Audio**: Automatic optimization handles most use cases

---

## Future Enhancements

- [ ] Integrate D-ID or SadTalker for professional lip-sync
- [ ] Add background video support
- [ ] Implement custom music upload
- [ ] Add watermark/branding overlay
- [ ] Batch video generation
- [ ] Video quality presets
- [ ] Analytics integration
- [ ] Cloud storage integration (Google Drive, AWS S3)

---

## License

This project is proprietary to City Pathology Laboratory. All rights reserved.

---

## Support & Feedback

For issues, feature requests, or technical support:
- Email: support@citypathlab.in
- Phone: Available on City Pathology Laboratory website

---

## About City Pathology Laboratory

City Pathology Laboratory is a leading diagnostic center committed to providing accurate, reliable, and timely pathology services to the community.

---

## Deployment

### Option 1: Streamlit Cloud (Recommended) ⭐

**Streamlit Cloud is the official and easiest way to deploy Streamlit apps.**

1. **Push code to GitHub** (Already done!)
2. **Visit** https://share.streamlit.io/
3. **Sign in** with your GitHub account
4. **Click "New app"**
5. **Select repository**: citypathologylaboratory-svg/city-pathology-promo-video-generator
6. **Select branch**: main
7. **Select file**: app.py
8. **Click "Deploy"**

**App will be live at**: `https://share.streamlit.io/citypathologylaboratory-svg/city-pathology-promo-video-generator`

**Advantages:**
- ✅ Free hosting with automatic SSL
- ✅ Auto-deploys on GitHub push
- ✅ Full FFmpeg & moviepy support
- ✅ Built for Streamlit apps
- ✅ Easy secret management
- ✅ Automatic scaling

### Option 2: Vercel with Docker (Advanced)

For Vercel deployment, create a Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Then deploy:
```bash
vercel --prod
```

### Option 3: Docker Hub / AWS / GCP

Use the Dockerfile above with any container hosting platform.

---

**Website:** www.citypathlab.in
**Location:** Mehsana, Gujarat, India
