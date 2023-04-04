import pytest
from school_schedule.student import Student

def test_instantiate_valid_student():
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    assert quinn.name == "Quinn"
    assert len(quinn.classes) == 6
    assert quinn.grade == "junior"

def test_add_class():
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    
    quinn.add_class("Biology")

    assert len(quinn.classes) == 7

def test_get_num_classes():
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
    class_len = quinn.get_num_classes()

    assert class_len == 6

def test_summary():
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

    test_str = "Quinn is a junior. Quinn takes 6 classes: Pre-Calc, English III, World History, Gym, Chemistry, Music Composition"

    assert quinn.summary() == test_str

def test_empty_class_list():
    quinn = Student(
                "Quinn", 
                "junior", 
                []
            )
    
    assert len(quinn.classes) == 0
    assert quinn.get_num_classes() == 0

def test_classes_not_a_list():
    quinn = Student(
                "Quinn", 
                "junior", 
                "physics"
            )
    
    with pytest.raises(AttributeError):
        quinn.add_class("chemistry")

def test_grade_not_a_str():
    
    with pytest.raises(AttributeError):
        Student(
                "Quinn", 
                10, 
                []
            )