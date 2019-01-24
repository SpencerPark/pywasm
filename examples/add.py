import pywasm
pywasm.on_debug()

vm = pywasm.load('./examples/add.wasm')
r = vm.exec('add', [40, 2])
print(r)  # 42
