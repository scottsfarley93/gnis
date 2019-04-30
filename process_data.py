from pprint import pprint
READ_FILE = "./allfeatures.txt"
WRITE_FILE = "./nature_features_2.py"

allowed_categories = {
 'Arch': 720,
 'Arroyo': 466,
 'Bar': 5874,
 'Basin': 4295,
 'Bay': 13859,
 'Beach': 2412,
 'Bench': 728,
 'Bend': 2790,
 'Cape': 16241,
 'Channel': 3892,
 'Cliff': 4477,
 'Crater': 248,
 'Dam': 56907,
 'Falls': 2531,
 'Flat': 10343,
 'Forest': 1312,
 'Gap': 8284,
 'Glacier': 1019,
 'Gut': 3506,
 'Harbor': 1271,
 'Island': 20550,
 'Isthmus': 28,
 'Lake': 70091,
 'Lava': 168,
 'Levee': 545,
 'Pillar': 2100,
 'Plain': 289,
 'Range': 2496,
 'Rapids': 1067,
 'Reservoir': 73159,
 'Ridge': 15074,
 'Sea': 29,
 'Slope': 395,
 'Spring': 38674,
 'Stream': 231653,
 'Summit': 70736,
 'Swamp': 7632,
 'Valley': 70013,
 'Woods': 685}

state_summary = {}


category_summary = {}
read_handle = open(READ_FILE, 'r')
write_handle = open(WRITE_FILE, 'w')


for line in read_handle:
    row =  line.split("|")
    newrow = [row[1], row[2], row[3], row[9], row[10], row[17]]
    state = row[3]
    if state not in state_summary:
        state_summary[state] = 0
    category = row[2]
    if category in allowed_categories:
        writerow = ",".join(newrow) + "\n"
        write_handle.write(writerow)

pprint(state_summary)