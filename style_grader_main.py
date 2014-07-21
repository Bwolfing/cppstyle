#!/usr/bin/python
from style_grader_functions import print_success
from StyleRubric import StyleRubric

def main():
    rubric = StyleRubric()

    for filename in rubric.student_files:
        rubric.grade_student_file(filename)
        rubric.outside_main = True

    rubric.adjust_errors()

    #if you are not outside main, then it means you found a main
    rubric.print_errors(not rubric.outside_main)

#For debugging purposes only
    print "Total Errors: " + str(rubric.total_errors)
    for x, y in rubric.error_types.items():
        print x, y
 
if __name__ == '__main__':
    main()
