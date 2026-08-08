# MarkL.spec
import sys
from pathlib import Path

block_cipher = None
base_dir = Path(SPECPATH)

a = Analysis(
    ['main.py'],
    pathex=[str(base_dir)],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('core', 'core'),
        ('memory', 'memory'),
        ('actions', 'actions'),
        ('ui.py', '.'),
        ('face.png', '.'),
    ],
    hiddenimports=[
        'google.genai',
        'google.generativeai',
        'PyQt6.sip',
        'sounddevice',
        'psutil',
        'cv2',
        'PIL',
        'pynvml',
        'wmi',
        'win32com.client',
        'comtypes',
        'pycaw',
        'pywinauto',
        'pyautogui',
        'playwright',
        'duckduckgo_search',
        'youtube_transcript_api',
        'python_pptx',
        'fastapi',
        'uvicorn',
        'cryptography',
        'qrcode',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'tkinter', 'numpy.random._examples'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MARK-L',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # <-- No console window on Windows
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(base_dir / 'config' / 'jarvis.ico') if (base_dir / 'config' / 'jarvis.ico').exists() else None,
)

# macOS .app bundle
app = BUNDLE(
    exe,
    name='MARK-L.app',
    icon=str(base_dir / 'config' / 'jarvis.icns') if (base_dir / 'config' / 'jarvis.icns').exists() else None,
    bundle_identifier='com.fatihmakes.markl',
)
