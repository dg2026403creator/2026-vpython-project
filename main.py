Web VPython 3.2

scene.background = color.white
scene.width = 800
scene.height = 700
scene.center = vector(0,3,0)

road = box(pos=vector(0,0,0),
           size=vector(20,0.2,6),
           color=vector(0.5,0.5,0.5))

head = sphere(pos=vector(0,5,0),
              radius=0.7,
              color=color.orange)

neck = cylinder(pos=vector(0,4.3,0),
                axis=vector(0,0.5,0),
                radius=0.3,
                color=color.orange)

chest = ellipsoid(pos=vector(0,3.8,0),
                  length=1.8,
                  height=1.2,
                  width=0.8,
                  color=color.orange)

belly = ellipsoid(pos=vector(0,2.9,0),
                  length=1.1,
                  height=1,
                  width=0.7,
                  color=color.orange)

left_arm = cylinder(pos=vector(-0.8,4,0),
                    axis=vector(-0.5,-1,0),
                    radius=0.3,
                    color=color.orange)

right_arm = cylinder(pos=vector(0.8,4,0),
                     axis=vector(0.5,-1,0),
                     radius=0.3,
                     color=color.orange)

left_hand = sphere(pos=vector(-1.3,3,0),
                   radius=0.3,
                   color=color.orange)

right_hand = sphere(pos=vector(1.3,3,0),
                    radius=0.3,
                    color=color.orange)

pants = box(pos=vector(0,2,0),
            size=vector(1.2,0.8,0.6),
            color=color.blue)

left_leg = cylinder(pos=vector(-0.3,1.6,0),
                    axis=vector(0,-1.2,0),
                    radius=0.25,
                    color=color.orange)

right_leg = cylinder(pos=vector(0.3,1.6,0),
                     axis=vector(0,-1.2,0),
                     radius=0.25,
                     color=color.orange)

left_foot = sphere(pos=vector(-0.3,0.25,0),
                   radius=0.3,
                   color=color.blue)

right_foot = sphere(pos=vector(0.3,0.25,0),
                    radius=0.3,
                    color=color.blue)

body = [head, neck, chest, belly,
        left_arm, right_arm,
        left_hand, right_hand,
        pants, left_leg, right_leg,
        left_foot, right_foot]

speed = 0.1

while True:
    rate(60)

    keys = keysdown()

    if 'w' in keys:
        for part in body:
            part.pos.z = part.pos.z - speed

    if 's' in keys:
        for part in body:
            part.pos.z = part.pos.z + speed

    if 'a' in keys:
        for part in body:
            part.pos.x = part.pos.x - speed

    if 'd' in keys:
        for part in body:
            part.pos.x = part.pos.x + speed
