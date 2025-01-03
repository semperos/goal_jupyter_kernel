import json
import os
import shutil
import sys
from tempfile import TemporaryDirectory

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from jupyter_client.kernelspec import KernelSpecManager

kernel_json = {
    # "argv": [sys.executable, "-m", "goal_jupyter_kernel", "-f", "{connection_file}"],
    "argv": ["python3", "-m", "goal_jupyter_kernel", "-f", "{connection_file}"],
    "display_name": "Goal",
    "language": "text",
}


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        here = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(0, here)
        prefix = os.path.join(here, "data_kernelspec")

        with TemporaryDirectory() as td:
            os.chmod(td, 0o755)  # Starts off as 700, not user readable
            with open(os.path.join(td, "kernel.json"), "w") as f:
                json.dump(kernel_json, f, sort_keys=True)
            print("Installing Jupyter kernel spec")

            # Requires logo files in kernel root directory
            cur_path = os.path.dirname(os.path.realpath(__file__))
            for logo in ["logo-32x32.png", "logo-64x64.png"]:
                try:
                    shutil.copy(os.path.join(cur_path, logo), td)
                except FileNotFoundError:
                    print("Custom logo files not found. Default logos will be used.")

            KernelSpecManager().install_kernel_spec(
                td, "goal", user=False, prefix=prefix
            )
