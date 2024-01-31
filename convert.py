"""Convert file from ecan to one for quiz."""
import os

SOURCE_DIRECTORY = "src"
DEST_DIRECTORY = "dst"


def convert_file(filename, suffix="", exclude=None):
    """Convert file from ecan to one for quiz."""
    with open(f"{SOURCE_DIRECTORY}/{filename}") as infile:
        name, extension = filename.split(".")
        with open(f"{DEST_DIRECTORY}/{name}{suffix}.{extension}", "w") as outfile:
            lines = infile.read().splitlines()
            outfile.write(lines[0] + "\n")
            for line in lines[1:]:
                site_no, datetime, flowrate = line.split(",")
                date, time = datetime.split(" ", 1)
                day, _ = date.split("/", maxsplit=1)
                if int(day) > 30:
                    continue
                day = f"{int(day):02d}"
                time, afternoon = time.split(" ")
                afternoon = True if afternoon == "PM" else False
                hour, _ = time.split(":", maxsplit=1)

                if not afternoon and hour == "12":
                    hour = 0
                if afternoon and not hour == "12":
                    hour = int(hour) + 12
                hour = f"{int(hour):02d}"
                outline = f"{site_no},{day + hour},{flowrate}\n"
                outfile.write(outline)


def main():
    filenames = os.listdir(SOURCE_DIRECTORY)
    print(filenames)
    for filename in filenames:
        print(f"Converting file: {filename}")
        convert_file(filename)
        print(f"Done!")


main()
