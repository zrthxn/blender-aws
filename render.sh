read -p "Enter filename to render: " filename
echo

sudo /home/ec2-user/blender-2.92/blender -b $filename \
  --use-extension 1 \
  -E CYCLES \
  -t 0 \
  -P "config.py"