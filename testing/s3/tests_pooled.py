import a as a

def test_s1_a():
    assert a.a() == 42

import a as b

def test_s2_a():
    assert b.a() == 42

import a as a

def test_s3_a():
    assert a.a() == 42
