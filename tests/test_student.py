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