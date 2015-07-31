from itertools import *
import pytest
import os
import sys

def main():
    if len(sys.argv) > 1:
        wd = sys.argv[1]
    else:
        wd = '.'
    student_dirs = filter(os.path.isdir, os.listdir(wd))
    students     = []
    for sdir in student_dirs:
        os.path.join(wd, sdir)
        class Student:
            name    = sdir
            dirname = os.path.join(wd, sdir)
        students.append(Student)
    for s in students:
        for fname in os.listdir(s.dirname):
            if fname.startswith('test_'):
                s.code = open(os.path.join(s.dirname, fname)).read()
                s.code = s.code.replace('def test_',
                                        'def test_' + s.name + '_')
    code = '\n'.join( s.code for s in students )
    pooled_test_paths = []
    for s in students:
        path = os.path.join(s.dirname, 'tests_pooled.py')
        fw = open(path, 'w')
        fw.write(code)
        fw.close()
        print 'Written', path
        pooled_test_paths.append(path)
        init_path = os.path.join(s.dirname, '__init__.py')
        if not os.path.isfile(init_path):
            open(init_path, 'w').close()
    for path in pooled_test_paths:
        pytest.main(['--color=no', path])


main()
