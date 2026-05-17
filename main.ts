input.onButtonPressed(Button.AB, function () {
    Acebott.LCD1602_ShowString(0, 0, "Hola Mario")
    Acebott.LCD1602_CreateCharacter(CharIndex.C1, Acebott.LCD1602_CharacterPixels(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `))
    Acebott.LCD1602_Showchararacter(7, 1, CharIndex.C1)
})
Acebott.LCD1602_Init()
