import unittest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBootImageExtractor(unittest.TestCase):
    """
    Provides unit tests for the Boot Image Extractor script to ensure its proper functionality
    in various scenarios. Additional test cases can be added to improve test coverage.
    """
    
    def test_print_banner(self):
        from scripts.boot_image_extractor import print_banner
        with patch('builtins.print') as mock_print:
            print_banner("Test Banner")
            mock_print.assert_called_once()
            
    @patch('builtins.print')
    @patch('subprocess.getoutput')
    @patch('os.geteuid', MagicMock(return_value=0))
    def test_extract_boot_image_single_slot(self, mock_getoutput, mock_print):
        mock_getoutput.return_value = '/dev/block/boot'
        with patch('subprocess.check_call', MagicMock()) as mock_check_call:
            with patch('os.path.basename', MagicMock(return_value='test')):
                with patch('subprocess.getoutput', MagicMock(return_value='a')):
                    from scripts.boot_image_extractor import extract_boot_image_single_slot
                    extract_boot_image_single_slot('boot_path')
                    mock_check_call.assert_called_with(['dd', 'if=boot_path', 'of=./boot.img'])
                    
    @patch('builtins.print')
    @patch('subprocess.getoutput')
    @patch('os.geteuid', MagicMock(return_value=0))
    def test_extract_boot_image_dual_slot(self, mock_getoutput, mock_print):
        mock_getoutput.side_effect = ['/dev/block/boot_a', '/dev/block/boot_b', 'a']
        with patch('builtins.input', return_value='a'):
            with patch('subprocess.check_call', MagicMock()) as mock_check_call:
                with patch('os.path.basename', MagicMock(return_value='test')):
                    with patch('subprocess.getoutput', MagicMock(return_value='a')):
                        from scripts.boot_image_extractor import extract_boot_image_dual_slot
                        extract_boot_image_dual_slot('boot_a_path', 'boot_b_path')
                        mock_check_call.assert_called_with(['dd', 'if=boot_a_path', 'of=./boota.img'])
                        

if __name__ == '__main__':
    unittest.main()
