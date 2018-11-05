# Enter script code
store.set_global_value('hotkey', '<ctrl>+k')
engine.set_return_value('<shift>+<end>')
engine.set_return_value('<delete>')
engine.run_script('combo')