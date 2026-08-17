# Python Image Filter Studio
# This program lets the user add different filters to an image

from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


# Opens the image
def load_image(path):
    image = Image.open(path)
    return image.convert("RGB")


# Adds the filter the user chooses
def apply_filter(image, choice):

    # Makes the image grayscale
    if choice == "1":
        return ImageOps.grayscale(image).convert("RGB")

    # Blurs the image
    elif choice == "2":
        return image.filter(ImageFilter.BLUR)

    # Makes the image sharper
    elif choice == "3":
        return image.filter(ImageFilter.SHARPEN)

    # Shows the edges in the image
    elif choice == "4":
        return image.filter(ImageFilter.FIND_EDGES)

    # Makes the image brighter
    elif choice == "5":
        brightness = ImageEnhance.Brightness(image)
        return brightness.enhance(1.5)

    # Adds more contrast
    elif choice == "6":
        contrast = ImageEnhance.Contrast(image)
        return contrast.enhance(1.5)

    # Makes the image strong black and white
    elif choice == "7":
        gray_image = ImageOps.grayscale(image)

        black_white = gray_image.point(
            lambda pixel: 0 if pixel < 128 else 255
        )

        return black_white.convert("RGB")

    else:
        return None


# Shows the options
def show_menu():

    print("\n============================")
    print(" Python Image Filter Studio")
    print("============================")

    print("1. Grayscale")
    print("2. Blur")
    print("3. Sharpen")
    print("4. Edge Detection")
    print("5. Increase Brightness")
    print("6. Increase Contrast")
    print("7. Black & White Silhouette")
    print("8. Exit")


# Main part of the program
def main():

    print("\nWelcome to Python Image Filter Studio")

    # User enters the image location
    image_path = input("\nEnter the path to an image: ").strip()

    # Checks if the image is there
    if not Path(image_path).exists():
        print("\nImage not found.")
        return

    image = load_image(image_path)

    while True:

        show_menu()

        choice = input("\nChoose an option: ").strip()

        # Exits the program
        if choice == "8":
            print("\nClosing Image Filter Studio.")
            break

        # Adds the filter
        filtered_image = apply_filter(image, choice)

        if filtered_image is None:
            print("\nInvalid option. Choose 1 through 8.")
            continue

        # User chooses a name for the new image
        output_name = input(
            "\nEnter a name for the new image (example: result.jpg): "
        ).strip()

        # Gives it a name if the user leaves it blank
        if output_name == "":
            output_name = "filtered_result.jpg"

        # Adds .jpg if the user forgets the file type
        if "." not in output_name:
            output_name = output_name + ".jpg"

        # Saves the finished image
        filtered_image.save(output_name)

        print("\nImage filter completed.")
        print("Saved as:", output_name)


# Runs the program
if __name__ == "__main__":
    main()