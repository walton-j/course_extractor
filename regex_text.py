# regex_text
import re
import pandas as pd
from typing import List, Union

filename = 'EngMgt.txt'

with open(filename, 'r') as f:
        lines = f.readlines()

course_data = {
        'course_number': [],
        'course_name': [],
        'class': [],
        'section_info': [],
        'occurrences': [],
        'arrangements': [],
        'room': [],
        'instructors': []
}

for i, line in enumerate(lines):
    if re.search(r"([A-Z]+(?:\s+[A-Z]+)?\s+\d+)\s*-\s*(.*)", line) and "-" in line and 'Collapsible' not in line:

        # pulling course name & number
        course_num, course_title = line.split(" - ", 1)
        course_data['course_number'].append(course_num) # pulls course name
        course_data['course_name'].append(course_title)

        # The rest
        course_data['class'].append(lines[i + 2]) # course
        course_data['section_info'].append(lines[i + 3])
        course_data['occurrences'].append(lines[i + 4])
        course_data['arrangements'].append(lines[i + 5])
        course_data['room'].append(lines[i + 6])

        instructor_list = []
        for j in range(i + 7, len(lines)):
            if re.match(r"^[A-Za-z .,'-]+$", lines[j].strip()):
                instructor_list.append(lines[j])
            else:
                if instructor_list:
                    instructor_str = ", ".join(instructor_list)
                    course_data['instructors'].append(", ".join(instructor_list))
                    break