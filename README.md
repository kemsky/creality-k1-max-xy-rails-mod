# Creality K1 Max XY Rails Mod

## Description

This mod fixes K1 Max quality issues, namely excessive ringing/echo. It also increases maximum accelerations.

This mod uses MGN12 rails for X and Y axis.

Also, it uses POWGE 7.7 mm belt and corresponding idler pulleys, 
but you can use 6 mm belt with stock idlers if you add washers to compensate size differences (POWGE idlers have 10.4 mm height).

[Washers 0.2mm (Affiliate)](https://s.click.aliexpress.com/e/_Dn3ZZa3)

[Washers 0.3mm (Affiliate)](https://s.click.aliexpress.com/e/_DEptgHN)

There are two versions of toolhead: one for rails only and one for rails reinforced with 20x10 pipe.

You must use camera mount from this mod, it is 8mm lower than original.

All rails must be cut to have 375 mm between far left and far right holes, X axis rail has max 410 mm total length (375 + 17.5x2), 
Y axis rails have max 394 mm total length (safe to use 375 + 2x9 mm).

Recommended printing materials:

- Toolhead - PA-6 or similar
- Other parts - ABS-GF/ABS-CF

### License

All work in this repository falls under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

https://creativecommons.org/licenses/by-nc-sa/4.0/

### Notes

Partially this work is based on [D3vil-Design](https://github.com/D3vil-Design/K1-Hardware-Mods) and [Henlor](https://www.printables.com/@Henlor) designs.

## Photos

![front view](/images/assembled/IMG_20240616_014701.jpg)
![top view](/images/assembled/IMG_20240616_014719.jpg)
![motor mount](/images/assembled/IMG_20240616_014727.jpg)
![joint](/images/assembled/IMG_20240616_014730.jpg)
![front idler](/images/assembled/IMG_20240616_014735.jpg)
![toolhead](/images/assembled/IMG_20240616_014742.jpg)

## Input shaper graphs

Input shaper graphs for reinforced X axis (20x5mm aluminium + 20x5mm carbon).

![X axis](/images/parts/x_axis.jpg)

**(!) Results for Y axis will be worse (two peaks) when X axis is not reinforced or aluminum pipe 20x10x2 is used.**

### X axis
![X axis](/images/resonances_x.png)

### Y axis
![Y axis](/images/resonances_y.png)

# BOM

BOM contains affiliate links, this way you can support my work if you want.

## Front Idlers

![Front Idler](/images/parts/front_idlers.jpg)

### Left

| Item                            | Type      | Count | Link                                                  |
|---------------------------------|-----------|-------|-------------------------------------------------------|
| DIN 7991 Flat Head Cap Screw    | M4 30 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DkdOkeJ) |
| DIN 7991 Flat Head Cap Screw    | M3 6 mm   | 4     | [AliExpress](https://s.click.aliexpress.com/e/_DmfmqJh) |
| DIN 912 Socket Head Cap Screw   | M3 16 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm    | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 5x5 mm | 5     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

### Right

| Item                            | Type      | Count | Link                                                    |
|---------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 7991 Flat Head Cap Screw    | M4 30 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DkdOkeJ) |
| DIN 7991 Flat Head Cap Screw    | M3 6 mm   | 4     | [AliExpress](https://s.click.aliexpress.com/e/_DmfmqJh) |
| DIN 912 Socket Head Cap Screw   | M3 16 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm    | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 5x5 mm | 5     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

## Joints

![Joint](/images/parts/joints.jpg)

### Left

| Item                            | Type      | Count | Link                                                    |
|---------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 7991 Flat Head Cap Screw    | M4 30 mm  | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DkdOkeJ) |
| Flat Thin Wafer Head Screw      | M3 6 mm   | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DFHDPnH) |
| DIN 912 Socket Head Cap Screw   | M3 8 mm   | 3     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| DIN 912 Socket Head Cap Screw   | M3 25 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm    | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 5x5 mm | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

### Right

| Item                            | Type      | Count | Link                                                    |
|---------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 7991 Flat Head Cap Screw    | M4 30 mm  | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DkdOkeJ) |
| Flat Thin Wafer Head Screw      | M3 6 mm   | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DFHDPnH) |
| DIN 912 Socket Head Cap Screw   | M3 8 mm   | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| DIN 912 Socket Head Cap Screw   | M3 25 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm    | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 5x5 mm | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

## Rails mounts (you'll need at least 2 of these)

![Motor Mounts](/images/parts/rails_mount.jpg)

| Item                            | Type      | Count | Link                                                    |
|---------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 912 Socket Head Cap Screw   | M3 25 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| Heat insert                     | M3 5x5 mm | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

### Right

| Item                          | Type      | Count | Link                                                    |
|-------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 912 Socket Head Cap Screw | M3 25 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| Heat insert                   | M3 5x5 mm | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |



## Motor Mounts

![Motor Mounts](/images/parts/motor_mounts.jpg)

### Left

| Item                            | Type      | Count | Link                                                    |
|---------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 7991 Flat Head Cap Screw    | M3 6 mm   | 4     | [AliExpress](https://s.click.aliexpress.com/e/_DmfmqJh) |
| DIN 912 Socket Head Cap Screw   | M3 6 mm   | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| DIN 912 Socket Head Cap Screw   | M3 16 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm    | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 5x5 mm | 6     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

### Right

| Item                            | Type      | Count | Link                                                    |
|---------------------------------|-----------|-------|---------------------------------------------------------|
| DIN 7991 Flat Head Cap Screw    | M3 6 mm   | 4     | [AliExpress](https://s.click.aliexpress.com/e/_DmfmqJh) |
| DIN 912 Socket Head Cap Screw   | M3 6 mm   | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| DIN 912 Socket Head Cap Screw   | M3 16 mm  | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm    | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 5x5 mm | 6     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

## Tensioners

![Motor Mounts](/images/parts/tensioners.jpg)

### Left

| Item                            | Type        | Count | Link                                                    |
|---------------------------------|-------------|-------|---------------------------------------------------------|
| DIN 912 Socket Head Cap Screw   | M3 45 mm    | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DCYZ5zD) |
| DIN 912 Socket Head Cap Screw   | M3 16 mm    | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| DIN 912 Socket Head Cap Screw   | M4 20 mm    | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DEOTbEL) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm      | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 3x4.5 mm | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |

### Right

| Item                            | Type        | Count | Link                                                    |
|---------------------------------|-------------|-------|---------------------------------------------------------|
| DIN 912 Socket Head Cap Screw   | M3 45 mm    | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DCYZ5zD) |
| DIN 912 Socket Head Cap Screw   | M3 16 mm    | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DDrYqiJ) |
| DIN 912 Socket Head Cap Screw   | M4 20 mm    | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DEOTbEL) |
| POWGE GT2 No Teeth Idler Pulley | 7.7 mm      | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DeapZjH) |
| Heat insert                     | M3 3x4.5 mm | 2     | [AliExpress](https://s.click.aliexpress.com/e/_DeBGks7) |


## Toolhead

There are 3 options: 
1. only rail 
2. rail + 20x10 pipe
3. rail + 20x5 carbon + 20x5 aluminium.

// todo: add items and links

## Other parts

7.7 mm belts increase max accelerations, aluminum pipe improves rigidity of the X axis,
though it will not provide enough rigidity to have single peak on Y axis.

Personally, I'm using 20x5 mm carbon board and 20x5 mm aluminum boards combined instead of 20x10x2 mm pipe. 
This items can be found in your local hardware store or on AliExpress.

| Item                       | Type           | Count | Link                                                                                                                                          |
|----------------------------|----------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| POWGE GT2 belt             | 7.7 mm         | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DkK1xL9)                                                                                       |
| Aluminium rectangular pipe | 20x10x2x500 mm | 1     | [AliExpress](https://s.click.aliexpress.com/e/_Defnblp)                                                                                       |

## Tools (Optional)

Thins you might need, drill bits, taps.

| Item                | Type | Count | Link                                                    |
|---------------------|------|-------|---------------------------------------------------------|
| Hand Tap            | 3 mm | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DEEnHLH) |
| Hand Tap Wrench     |      | 1     | [AliExpress](https://s.click.aliexpress.com/e/_DFq7575) |
| HSS Drill Bits Set  |      | 1     | [AliExpress](https://s.click.aliexpress.com/e/_Dmw4uhz) |