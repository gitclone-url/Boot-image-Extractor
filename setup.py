# BootImageExtractor Setup File
# -----------------------------
# 
# Install with: pip install .
#
# Usage: sudo boot_image_extractor.py or su -c 'boot_image_extractor.py'
#

from setuptools import setup

setup(
    name='Boot-Image-Extractor',
    scripts=['scripts/boot_image_extractor.py'],
    install_requires=[
        'pyfiglet',
    ],
)
