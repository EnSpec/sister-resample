import glob
import os


def main():

    # Unzip and untar granules
    input_dir = "input"

    dirs = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]
    instrument = "PRISMA" if dirs[0][:3] == "PRS" else "AVIRIS"

    # Get paths based on product type file matching
    paths = []

    if instrument == "PRISMA":
        paths+= glob.glob(os.path.join(input_dir, "*", "*rfl_prj"))

    elif instrument == "AVIRIS":
        paths+= glob.glob(os.path.join(input_dir, "*", "*_ort_img"))
        paths+= glob.glob(os.path.join(input_dir, "*", "*_img"))
        paths+= glob.glob(os.path.join(input_dir, "*", "*obs_ort"))
        paths+= glob.glob(os.path.join(input_dir, "*", "*loc"))
        paths+= glob.glob(os.path.join(input_dir, "*", "*_ort_igm"))
        paths+= glob.glob(os.path.join(input_dir, "*", "*rfl*"))
        paths+= glob.glob(os.path.join(input_dir, "*", "*corr*img"))

    for path in paths:
        if not path.endswith('.hdr'):
            print(path)

if __name__ == "__main__":
    main()
