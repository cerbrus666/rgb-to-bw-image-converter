import cv2
import argparse


def colour_to_gray(file_path, output_path):
    image_mat = cv2.imread(file_path, flags=cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(image_mat, cv2.COLOR_BGR2GRAY)
    status = cv2.imwrite(output_path, img_gray)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", help="3-channels rgb input image path to be converted"
    )
    parser.add_argument("-o", "--output", help="1-channel output image path result")
    args = parser.parse_args()
    colour_to_gray(args.input, args.output)
