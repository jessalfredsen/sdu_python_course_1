from datetime import datetime


def goodmorning_sdu():
    """En funktion der viser hvad en funktion kan."""
    
    _now = datetime.now()
    
    print(f"Glædelig kursus dag SDU'ere! Klokken er lige nu {_now}")
    
    return _now


def load_data():
    return [1,2,3,4,5,5,6]


if __name__ == '__main__':
    goodmorning_sdu()