import os
import string

tradefile = open("traderes.txt", "w+")
locfile = open("locres.txt", "w+")
gfxfile = open("gfxres.txt", "w+")
gfxfile.write("spriteTypes = {\n\n")
names = []
for filename in os.listdir():
    if filename.endswith(".dds"):
        names.append(filename[:-4])
        resource_name = filename[6:-4]
        resource_loc  = resource_name.replace("_", " ")
        gfxfile.write(f"\tspriteType = {{\n\t\tname = \"GFX_text_{resource_name}\"\n\t\ttextureFile = \"gfx/interface/icons/text_icons/{filename}\"\n\t}}\n\n")
        locfile.write(f" trade_action_r_{resource_name}: \"£{resource_name}£ $r_{resource_name}$\"\n trade_action_r_{resource_name}_desc: \"Trade away our £{resource_name}£ $r_{resource_name}$ relic.\"\n\n")
        tradefile.write(f"trade_action_r_{resource_name} = {{\n\tfire_and_forget = yes\n\n\tpotential = {{\n\t\thas_relic = r_{resource_name}\n\t\tis_country_type = default\n\t\tfrom = {{\n\t\t\tis_country_type = default\n\t\t\tnot = {{ has_relic = r_{resource_name} }}\n\t\t}}\n\t\tNOT = {{ has_modifier = relic_activation_cooldown }}\n\t}}\n\n\ton_traded_effect = {{\n\t\tremove_relic = r_{resource_name}\n\t\tfrom = {{ add_relic = r_{resource_name} }}\n\t}}\n\n\tai_weight = {{\n\t\tweight = 1000\n\t}}\n}}\n\n")

print(names)
gfxfile.write("}")