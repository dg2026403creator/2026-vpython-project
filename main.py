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
              texture="https://i.postimg.cc/mDgmMsvj/kaebcheo.png")

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

criminal_head = sphere(pos=vector(5,5,0),
                       radius=0.7,
                       color=color.orange)

criminal_body = ellipsoid(pos=vector(5,3.8,0),
                          length=1.8,
                          height=1.2,
                          width=0.8,
                          color=color.red)

criminal_belly = ellipsoid(pos=vector(5,2.9,0),
                           length=1.1,
                           height=1,
                           width=0.7,
                           color=color.red)

criminal_left_arm = cylinder(pos=vector(4.2,4,0),
                              axis=vector(-0.5,-1,0),
                              radius=0.3,
                              color=color.red)

criminal_right_arm = cylinder(pos=vector(5.8,4,0),
                               axis=vector(0.5,-1,0),
                               radius=0.3,
                               color=color.red)

criminal_left_hand = sphere(pos=vector(3.7,3,0),
                             radius=0.3,
                             color=color.orange)

criminal_right_hand = sphere(pos=vector(6.3,3,0),
                              radius=0.3,
                              color=color.orange)

criminal_pants = box(pos=vector(5,2,0),
                     size=vector(1.2,0.8,0.6),
                     color=color.black)

criminal_left_leg = cylinder(pos=vector(4.7,1.6,0),
                              axis=vector(0,-1.2,0),
                              radius=0.25,
                              color=color.black)

criminal_right_leg = cylinder(pos=vector(5.3,1.6,0),
                               axis=vector(0,-1.2,0),
                               radius=0.25,
                               color=color.black)

criminal_left_foot = sphere(pos=vector(4.7,0.25,0),
                            radius=0.3,
                            color=color.black)

criminal_right_foot = sphere(pos=vector(5.3,0.25,0),
                             radius=0.3,
                             color=color.black)

criminal = [criminal_head, criminal_body, criminal_belly,
            criminal_left_arm, criminal_right_arm,
            criminal_left_hand, criminal_right_hand,
            criminal_pants, criminal_left_leg,
            criminal_right_leg, criminal_left_foot,
            criminal_right_foot]

speed = 0.1
caught = False

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

    if head.pos.x > 3 and caught == False:
        for part in criminal:
            part.visible = False

        label(pos=head.pos,
              text="@200hyung",
              color=color.red)

        caught = True
