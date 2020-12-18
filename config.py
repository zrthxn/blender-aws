import bpy, _cycles

print('\u001b[33m', _cycles.available_devices('CUDA'), '\u001b[37m')

prop = bpy.context.preferences.addons['cycles'].preferences

prop.get_devices(prop.compute_device_type)
prop.compute_device_type = 'CUDA'

for device in prop.devices:
  if device.type == 'CUDA':
    print('\u001b[32m Using CUDA Device: ', device.name, '\u001b[37m')
    device.use = True

bpy.context.scene.cycles.device = 'GPU'

bpy.data.scenes["Scene"].render.filepath = "/home/ec2-user/output.png"
bpy.ops.render.render(write_still=True)