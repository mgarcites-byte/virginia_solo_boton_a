def on_logo_pressed():
    global brightess
    for index in range(25):
        brightess += 4
        Acebott.set_led_brightness(AnalogWritePin.P0, brightess)
    for index2 in range(25):
        brightess += -4
        Acebott.set_led_brightness(AnalogWritePin.P0, brightess)
        basic.pause(100)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    music.play(music.string_playable("C5 A E D G F B C ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_long_pressed():
    global brightess
    brightess = 0
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_b():
    music.play(music.string_playable("C5 B A G F D E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

brightess = 0
Acebott.RFID_init()
basic.clear_screen()
Acebott.LCD1602_Init()
music.set_built_in_speaker_enabled(True)
Acebott.Servo_IO(ServoPin.P16, 0)

def on_forever():
    Acebott.LCD1602_ShowString(0, 0, "Hello,Acebott!")
    if Acebott.pir_motion(DigitalPin.P0) == 1:
        basic.show_icon(IconNames.DUCK)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)

def on_forever2():
    serial.write_string("T:")
    serial.write_line("" + str((Acebott.DHT11_getvalue(DigitalWritePin.P8, DHT11Type.TEMPERATURE_C))))
    Acebott.LCD1602_ShowString(0, 0, "T:")
    Acebott.LCD1602_ShowNumber(2,
        0,
        Acebott.DHT11_getvalue(DigitalWritePin.P8, DHT11Type.TEMPERATURE_C))
    serial.write_string("H:")
    serial.write_line("" + str((Acebott.DHT11_getvalue(DigitalWritePin.P8, DHT11Type.HUMIDITY))))
    Acebott.LCD1602_ShowString(9, 0, "H:")
    Acebott.LCD1602_ShowNumber(11,
        0,
        Acebott.DHT11_getvalue(DigitalWritePin.P0, DHT11Type.HUMIDITY))
basic.forever(on_forever2)

def on_forever3():
    if Acebott.pir_motion(DigitalPin.P1) == 1:
        basic.show_icon(IconNames.DUCK)
    else:
        basic.clear_screen()
basic.forever(on_forever3)

def on_forever4():
    serial.write_string("Gas concentration:")
    serial.write_line("" + str((Acebott.MQ4_Sensor(AnalogReadPin.P2))))
    if Acebott.MQ4_Sensor(AnalogReadPin.P2) >= 500:
        music.set_built_in_speaker_enabled(True)
        music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        music.set_built_in_speaker_enabled(False)
basic.forever(on_forever4)

def on_forever5():
    if Acebott.RFID_getID() != 0:
        music.play(music.string_playable("C5 B A G F G B D ", 120),
            music.PlaybackMode.UNTIL_DONE)
        Acebott.Servo_IO(ServoPin.P16, 100)
        basic.pause(5000)
        Acebott.Servo_IO(ServoPin.P16, 10)
basic.forever(on_forever5)
