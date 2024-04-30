import argparse
import time
import numpy as np
import skrobot


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--interactive", action="store_true", help="enter interactive shell"
    )
    args = parser.parse_args()

    robot = skrobot.models.Kuka()

    viewer = skrobot.viewers.TrimeshSceneViewer(resolution=(640, 480))

    plane = skrobot.model.Box(extents=(2, 2, 0.01), face_colors=(0.75, 0.75, 0.75))
    viewer.add(plane)

    viewer.add(robot)

    viewer.set_camera(angles=[np.deg2rad(45), 0, 0], distance=4)

    viewer.show()

    box = skrobot.model.Box(extents=(0.05, 0.05, 0.05), face_colors=(1.0, 0, 0))
    box_pose = (0.5, 0, 0.7)
    box.translate(box_pose)
    viewer.add(box)

    robot.init_pose()

    # Compute the joint angles for this step
    robot.inverse_kinematics(box, rotation_axis="y")

    # Print the joint angles for this step
    print(robot.angle_vector())

    while not viewer.has_exit:
        time.sleep(0.1)
        viewer.redraw()


if __name__ == "__main__":
    main()
