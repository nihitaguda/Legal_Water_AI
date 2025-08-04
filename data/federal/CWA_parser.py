section_names = ["section 1267", "section 1281"]
extracted_texts = []
current_lines = []

with open("CleanWaterAct.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        strip = line.strip().lower()
        if strip in section_names:
            extracted_texts.append("\n".join(current_lines))
            current_lines = []
        current_lines.append(line)

# If the file ends and we were still collecting, save the last section
if (len(section_names) == len(extracted_texts)-1):
    extracted_texts.append("\n".join(current_lines))

print("Collected section count:", len(extracted_texts))
