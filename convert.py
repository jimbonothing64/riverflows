"""Convert file from ecan to one for quiz."""

FILENAMES = ["data.csv"]


def convert_file(filename, suffix="_converted", exclude=None):
    """Convert file from ecan to one for quiz."""
    with open(filename) as infile:
        name, extension = filename.split(filename)
        with open(f"{name}{suffix}.{extension}", "w") as outfile:
            lines = infile.read().splitlines()
            outfile.write(lines[0] + "\n")
            for line in lines[1:]:
                site_no, datetime, flowrate = line.split(",")
                date, time = datetime.split(" ", 1)
                day, _ = date.split("/", maxsplit=1)
                time, afternoon = time.split(" ")
                afternoon = True if afternoon == "PM" else False
                hour, _ = time.split(":", maxsplit=1)
                if afternoon:
                    hour = str(int(hour) + 12)
                outline = f"{site_no},{day + hour},{flowrate}\n"
                outfile.write(outline)


def main():
    for filename in FILENAMES:
        print(f"Converting file: {filename}")
        convert_file(filename)
        print(f"Done!")


main()
