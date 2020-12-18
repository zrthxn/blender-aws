## Blender Rendering Scripts

These are my scripts to run a Blender rendering engine on AWS P2.
You need to have permission to start a P2 instance. I've tested this with 
Tesla K80 Drivers and nVIDIA CUDA drivers.

### How to
- Start a p2.xlarge instance.
- Install K80 and CUDA drivers.
- Download [Blender](https://builder.blender.org/download/).
- Run `render.sh`