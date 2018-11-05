# Enter script code
store.set_global_value('hotkey', '<ctrl>+u')
engine.set_return_value('<shift>+<home>')
engine.set_return_value('<backspace>')
engine.run_script('combo')