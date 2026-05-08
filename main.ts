input.onButtonPressed(Button.A, function () {
    music.setBuiltInSpeakerEnabled(true)
    music.play(music.stringPlayable("D A E D B F B C ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    music.play(music.stringPlayable("C5 B A G F D E C ", 120), music.PlaybackMode.UntilDone)
})
