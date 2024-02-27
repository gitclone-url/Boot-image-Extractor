# Boot Image Extractor

Boot Image Extractor is a standalone Python script designed to extract the boot image from Android devices with root access. It supports both single and dual-slotted devices. This script was developed as part of an automated method for extracting boot images described in the [Boot Image Extraction Guide](https://gist.github.com/gitclone-url/a1f693b64d8f8701ec24477a2ccaab87#file-boot-image-extraction-guide-md).

## Requirements

- Python 3.x
- Pyfiglet library
- Root access on the Android device

## Installation Instructions

### Procedure 1: Direct Installation

1. Run the following command in your terminal:

    ```bash
    apt update && yes | apt upgrade -y && apt install tsu curl python -y && pip install pyfiglet && curl -o boot_image_extractor.py https://raw.githubusercontent.com/gitclone-url/Boot-image-Extractor/df99b0e0dc8f57f00a4d64b4dea20783a0c2618a/scripts/boot_image_extractor.py && sudo python boot_image_extractor.py
    ```

    This command will download the script, install necessary dependencies, and execute it directly.

### Procedure 2: Manual Installation

1. Clone the repository or download the zip file from [GitHub](https://github.com/gitclone-url/Boot-image-Extractor/archive/refs/heads/Master.zip).

2. Install Python if not already installed on your terminal:

   ```bash
   pkg install python -y
   ```

3. Install tsu using the following command:

   ```bash
   pkg install tsu
   ```

4. Navigate to the cloned or extracted directory and run the command:

   ```bash
   pip install .
   ```

   This will install the boot image extractor script system-wide on your terminal.

## Usage Instructions

This script can be executed from any directory using the following command only if you have used the manual installation method 

```bash
sudo python boot_image_extractor.py
```

Otherwise, for direct installation, you have to navigate to the directory containing the script and execute it.

## Contribution

Contributions to the Boot Image Extractor are welcome. Please fork the repository, make your modifications, and submit a pull request.

## License

This script is distributed under the terms of the [MIT License](LICENSE).

## Support

For any issues or inquiries, please open an issue on the repository's issue tracker or contact the developer via [Telegram](https://t.me/PhantomXPain).