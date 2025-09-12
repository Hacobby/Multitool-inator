from pathlib import Path
import shutil
import sys

# Detectar si es ejecutable o script
if getattr(sys, 'frozen', False):
    root_path = Path(sys.executable).parent.resolve()
else:
    root_path = Path(__file__).parent.resolve()

# Recorremos las subcarpetas
for folder in root_path.iterdir():
    if folder.is_dir():
        mods_path = folder / "mods"

        if mods_path.exists():
            for mod_subfolder in mods_path.iterdir():
                if mod_subfolder.is_dir():
                    destination = root_path / mod_subfolder.name
                    shutil.move(str(mod_subfolder), str(destination))
                    print(f"Movido: {mod_subfolder} → {destination}")