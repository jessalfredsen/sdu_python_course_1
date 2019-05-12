from datetime import datetime


def goodmorning_sdu():
    """En funktion der viser hvad en funktion kan."""
    
    _now = datetime.now()
    
    print(f"Glædelig kursus dag SDU'ere! Klokken er lige nu {_now}")
    
    return _now


if __name__ == '__main__':
    goodmorning_sdu()