def on_button_pressed_a():
    while True:
        pins.servo_write_pin(AnalogPin.P0, 0)
        basic.pause(500)
        if input.button_is_pressed(Button.B):
            break
        pins.servo_write_pin(AnalogPin.P0, 180)
        basic.pause(500)
        if input.button_is_pressed(Button.B):
            break

input.on_button_pressed(Button.A, on_button_pressed_a)