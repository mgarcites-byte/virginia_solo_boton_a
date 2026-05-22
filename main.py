def on_button_pressed_ab():
    Acebott.LCD1602_ShowString(0, 0, "Hola Mario")
    Acebott.LCD1602_CreateCharacter(CharIndex.C1,
        Acebott.LCD1602_CharacterPixels("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """))
    Acebott.LCD1602_Showchararacter(7, 1, CharIndex.C1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Acebott.LCD1602_Init()