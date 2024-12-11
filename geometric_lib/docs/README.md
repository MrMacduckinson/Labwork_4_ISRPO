# Math formulas
In general, this library consists of functions that return perimeter and area of some basic figures (circle, square, rectangle and triangle). Just pass the main characteristics (like the length of a side or the radius) to needed functions and get your answer.

## Circle
The functions are in `circle.py`.

### Area
`area(r)`\
Returns the area of a disk with radius `r`. 

#### Parameters
- `r (number)`: radius of a disk
            
#### Return value
- `math.pi * r * r (number)`: area of a disk with radius `r`

#### Example

##### Input
```
python3 -c "from circle import area; print(area(1.2))" 
```
##### Output
```
4.523893421169302
```

### Perimeter
`perimeter(r)`\
Returns the circumference of a circle with radius `r`. 

#### Parameters
- `r (number)`: radius of a circle
            
#### Return value
- `2 * math.pi * r (number)`: circumference of a circle with radius `r`

#### Example

##### Input
```
python3 -c "from circle import perimeter; print(perimeter(1.2))"
```
##### Output
```
7.5398223686155035
```

## Rectangle
The functions are in `rectangle.py`.

### Area
`area(a, b)`\
Returns the area of a rectangle with sides `a` and `b`.

#### Parameters
- `a (number)`: side `a` of a rectangle
- `b (number)`: side `b` of a rectangle
            
#### Return value
- `a * b (number)`: area of a rectangle with sides `a` and `b`

#### Example

##### Input
```
python3 -c "from rectangle import area; print(area(2.5, 4))"
```
##### Output
```
10.0
```

### Perimeter
`perimeter(a, b)`\
Returns the perimeter of a rectangle with sides `a` and `b`.

#### Parameters
- `a (number)`: side `a` of a rectangle
- `b (number)`: side `b` of a rectangle
            
#### Return value
- `a + b + a + b (number)`: perimeter of a rectangle with sides `a` and `b`

#### Example

##### Input
```
python3 -c "from rectangle import perimeter; print(perimeter(2.5, 4))"
```
##### Output
```
13.0
```

## Square
The functions are in `square.py`.

### Area
`area(a)`\
Returns the area of a square with side `a`.

#### Parameters
- `a (number)`: side of a square
            
#### Return value
- `a * a (number)`: area of a square with side `a`

#### Example

##### Input
```
python3 -c "from square import area; print(area(5))"
```
##### Output
```
25
```

### Perimeter
`perimeter(a)`\
Returns the perimeter of a square with side `a`.

#### Parameters
- `a (number)`: side of a square
            
#### Return value
- `4 * a (number)`: perimeter of a square with side `a`

#### Example

##### Input
```
python3 -c "from square import perimeter; print(perimeter(5))"
```
##### Output
```
20
```

## Triangle
The functions are in `triangle.py`.

### Area
`area(a, h)`\
Returns the area of a triangle with base `a` height `h` dropped to base `a`.

#### Parameters
- `a (number)`: base `a` of a triangle
- `h (number)`: height `h` dropped to base `a`
            
#### Return value
- `a * h / 2 (number)`: area of a triangle with base `a` height `h` dropped to base `a`

#### Example

##### Input
```
python3 -c "from triangle import area; print(area(2, 2))"
```
##### Output
```
2.0
```

### Perimeter
`perimeter(a, b, c)`\
Returns the perimeter of a triangle with sides `a`, `b` and `c`.

#### Parameters
- `a (number)`: side `a` of a triangle
- `b (number)`: side `b` of a triangle
- `c (number)`: side `c` of a triangle
            
#### Return value
- `a + b + c (number)`: perimeter of a triangle with sides `a`, `b` and `c`

#### Example

##### Input
```
python3 -c "from triangle import perimeter; print(perimeter(2, 2, 9.5))"
```
##### Output
```
13.5
```

# Changelog
```
commit 5550794de37653565e5d69e20623160b81f445d8 (HEAD -> new_features_466295)
Author: Mikhail Korsakov <mihasik.korsakov@gmail.com>
Date:   Wed Sep 25 22:56:17 2024 +0300

    added documentation to README.md

commit e54ba7fcc42589981cb4f58d3f79fe462fdf0f98
Author: Mikhail Korsakov <mihasik.korsakov@gmail.com>
Date:   Wed Sep 25 21:31:07 2024 +0300

    added descriptions for all functions

commit 6c15c7fe48369c9d84b7ccd361acf3da4d9635f8
Author: Mikhail Korsakov <mihasik.korsakov@gmail.com>
Date:   Wed Sep 25 14:51:36 2024 +0300

    restored the state of labwork_1

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```