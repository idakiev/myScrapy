import subprocess
ans = subprocess.call(['scrapy', 'crawl', 'shoes', '-o data.json'])
if ans == 0:
    print('Command executed.')
    subprocess.call(['python', 'clean_data.py'])
else:
    print('Command failed.')

# import re
#
# data = {
#     "availableColours": [
#         "\n                    Color White / Black01\n                    \n                    sElected  \n                  ",
#         "\n                    Color Brown\n                    \n                      \n                  ",
#         "\n                    Color White / Black02\n                    Clearance\n                     unavailable \n                  ",
#         "\n                    Color White / Bright Pink\n                    Clearance\n                     unavailable \n                  ",
#         "\n                    Color White / Multi\n                    Clearance\n                     unavailable \n                  "
#     ]
# }
#
# # List to store results
# color_status_list = []
#
# for entry in data["availableColours"]:
#     # Extract color
#     color_match = re.search(r"Color (.+)", entry)
#     color = color_match.group(1).strip() if color_match else "Unknown"
#
#     # Determine status
#     status = []
#     if "selected" in entry.lower():
#         status.append("Selected")
#     if "Clearance" in entry.lower():
#         status.append("Clearance")
#     if "unavailable" in entry.lower():
#         status.append("Unavailable")
#
#     # If no special status, mark as "Regular"
#     final_status = ", ".join(status) if status else "Regular"
#
#     # Append to list
#     color_status_list.append([color, final_status])
#
# # Print the result
# print(color_status_list)
