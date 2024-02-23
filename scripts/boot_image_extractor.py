#!/usr/bin/env python3

"""A script to extract boot image from either single or dual slotted Android devices with root access."""

import os
import sys
import pyfiglet
import subprocess

def print_banner(name):
    max_width = os.get_terminal_size().columns
    banner = pyfiglet.figlet_format(name, font='small', width=max_width)
    print(banner.center(max_width))
    
def exit_with_error(error, reason):
    print("\nError:", error)
    print("\nReason:", reason)
    sys.exit(1)
      
def extract_boot_image_dual_slot(boot_a_path, boot_b_path):
    active_slot = subprocess.getoutput('getprop ro.boot.slot_suffix')
    print("\nIt is recommended to extract the boot image according to the current active slot, which is ({}).\n".format(active_slot))

    while True:
        chosen_slot = input("Which boot slot image would you like to extract? (a/b): ").lower()
        if chosen_slot == 'a':
            boot_image_path = boot_a_path
            break
        elif chosen_slot == 'b':
            boot_image_path = boot_b_path
            break
        else:
            print("Invalid input. Please choose either 'a' or 'b'.\n")
            continue

    print("\nExtracting the boot image from {}...".format(boot_image_path))
    try:
        subprocess.check_call(['dd', 'if={}'.format(boot_image_path), 'of=./boot{}.img'.format(active_slot)])
        print("Boot image successfully extracted and saved in your {} directory.".format(os.path.basename(os.getcwd())))
    except subprocess.CalledProcessError:
        exit_with_error("Failed to extract the boot image", "dd command failed")

def extract_boot_image_single_slot(boot_path):
    print("\nExtracting the boot image from {}...".format(boot_path))
    try:
        subprocess.check_call(['dd', 'if={}'.format(boot_path), 'of=./boot.img'])
        print("Boot image successfully extracted and saved in your {} directory.".format(os.path.basename(os.getcwd())))
    except subprocess.CalledProcessError:
        exit_with_error("Failed to extract the boot image", "dd command failed")

def main():
    if os.geteuid() != 0:
        exit_with_error("Insufficient privileges", "This script requires root access. Please run as root or use sudo.")

    print_banner("Boot Image Extractor")

    boot_names = ['boot', 'boot_a', 'boot_b']
    for name in boot_names:
        path = subprocess.getoutput('find /dev/block -type l -name {} -print | head -n 1'.format(name))
        if path:
            print("{} = {}".format(name, path))
            if name == 'boot_a':
                boot_a_path = path
            elif name == 'boot_b':
                boot_b_path = path
            else:
                boot_path = path

    if 'boot_a_path' in locals() and 'boot_b_path' in locals():
        print("\nDevice has dual boot slots.")
        extract_boot_image_dual_slot(boot_a_path, boot_b_path)
    elif 'boot_path' in locals():
        print("\nDevice has a single boot slot.")
        extract_boot_image_single_slot(boot_path)
    else:
        exit_with_error("No boot slots found", "unable to find the symlinked boot slot files")

if __name__ == '__main__':
    main()