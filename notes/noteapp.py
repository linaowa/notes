import pygame
import time

pygame.mixer.init()

note_mapping = {
    1: "1do.wav",  # до
    2: "2re.wav",  # ре
    3: "3mi.wav",  # ми
    4: "4fa.wav",  # фа
    5: "5sol.wav",  # соль
    6: "6lja.wav",  # ля
    7: "7si.wav"   # си
}

def play_note(note_number):
    """
    Воспроизводит звуковой файл соответствующей ноты.

    Args:
        note_number (int): Номер ноты от 1 до 7.
    """
    if note_number < 1 or note_number > 7:
        print("Номер ноты должен быть от 1 до 7.")
        return
    
    sound_file = note_mapping[note_number]
    
    try:
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        time.sleep(sound.get_length())
    except pygame.error as e:
        print(f"Ошибка воспроизведения звука: {e}")

if __name__ == "__main__":
    try:
        note_number = int(input("введите номер ноты (от 1 до 7): "))
        play_note(note_number)
    except ValueError:
        print("неверный ввод. пожалуйста, введите целое число от 1 до 7.")