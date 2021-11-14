import anvil,os,re

REGION_FILES = "C:/Users/Masahiro Kuroda/Desktop/minecraft/1.18_testserver/world/region"
for file in [os.path.join(REGION_FILES,f) for f in os.listdir(REGION_FILES) if os.path.isfile(os.path.join(REGION_FILES,f))]:
    mca = re.search(r"r\.([\-0-9]+)\.([\-0-9]+)\.mca$",file)
    region_x = int(mca.group(1))
    region_z = int(mca.group(2))
    region = anvil.Region.from_file(file)
    for chunk_x in range(16,32):
        for chunk_z in range(16,32):            
            if region.chunk_location(chunk_x,chunk_z) != (0,0):
                chunk = region.get_chunk(chunk_x,chunk_z)            
                for x in range(16):
                    for y in range(-64,16):
                        for z in range(16):
                            block = chunk.get_block(x,y,z).name()
                            if block in ["minecraft:diamond_ore","minecraft:deepslate_diamond_ore"]:
                                print(str(x+chunk_x*16+region_x*512)+","+str(y)+","+str(z+chunk_z*16+region_z*512))
