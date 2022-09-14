# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:18:32 2022

@author: zwt
@email: 1030456532@qq.com
"""
import argparse
import os

from tqdm import tqdm
from utils.random_strings import COMMON_RU_MODE
from utils.random_strings import random_russian
from utils.generate import Style, generate_data

def parse():
    parser = argparse.ArgumentParser()
    # strings arguments.
    parser.add_argument('--count', type=int, default=10, help='the count of the screen shots.')
    parser.add_argument('--length', type=int, default=10, help='the length of the strings.')
    parser.add_argument('--group', type=int, default=4, help='the group of the strings. <- just like this sentence, group is 5.')
    
    # font style.
    parser.add_argument('--font_size', type=int, default=18, help='size of the letter. font size.')
    parser.add_argument('--font_color', type=int, nargs='+', default=(0, 0, 0), help='the strings font color.')
    parser.add_argument('--random_font_size', type=int, default=1, help='[0, 1] 0: stable font size, 1: multi size in [fontsize * 0.8, fontsize * 1.2].')
    
    # background style. 
    parser.add_argument('--background_size', type=int, nargs='+', default=(320, 160), help='the background img size. if u wanna set the bg just a lit bigger than strings size than just set it (0, 0). sure this param is small enough')
    parser.add_argument('--background_color', type=int, nargs='+', default=(255, 255, 255), help='the background color (RGB), if this param is not None then we will ignore the background_path.')
    parser.add_argument('--random_background_size', type=int, default=1, help='[0, 1] 0: stable background size, 1: multi size in [background size * 0.8, background size * 1.2].')
    parser.add_argument('--random_background_color', type=int, default=1, help='[0, 1] 0: stable color, 1: random color. if is 1, we will generate the color in [0, 255]')
    
    # path arguments.
    parser.add_argument('--save_path', type=str, default='./data', help='the path u wanna save the img data.')
    parser.add_argument('--font_path', type=str, default=None, help='the path for the font file.')
    parser.add_argument('--background_path', type=str, default=None, help='the path for the background file.')

    
    return parser
    
def main(opt):
    # Generate the style Class.
    style = Style(opt)

    for i in tqdm(range(opt.count), desc="generate data: ", ncols=80):
        # 1. random strings.
        strings = random_russian(opt.length, opt.group, COMMON_RU_MODE)

        # 2. generate the data pic. 
        bg, xmin, ymin, xmax, ymax = generate_data(opt, style, strings)

        # 3. save img.
        bg.save(os.path.join(opt.save_path, f"temp{i}.png"))

        # 4. save labels.
        print(f"\nxmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax}")

if __name__ == "__main__":
    opt = parse().parse_args()
    main(opt)