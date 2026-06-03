from pathlib import Path
import time

import mujoco
import mujoco.viewer
import numpy as np


XML_PATH = Path(__file__).with_name("simple_pendulum.xml")


def main() -> None:
    model = mujoco.MjModel.from_xml_path(str(XML_PATH))
    data = mujoco.MjData(model)

    data.qpos[0] = np.deg2rad(20.0)
    mujoco.mj_forward(model, data)

    with mujoco.viewer.launch_passive(model, data) as viewer:
        start = time.time()
        while viewer.is_running() and time.time() - start < 30:
            if data.time < 0.8:
                data.ctrl[0] = 0.3
            elif data.time < 1.4:
                data.ctrl[0] = -0.3
            else:
                data.ctrl[0] = 0.0

            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(model.opt.timestep)


if __name__ == "__main__":
    main()
