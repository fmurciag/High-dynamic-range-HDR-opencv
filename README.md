# Opencv-HDR-demo
High-dynamic-range tone mapping with a diferents algorithms

# Example

### Imputs
<table>
  <tr>
    <td>Exposure: 1/4s</td>
    <td>Exposure: 1/8s</td>
    <td>Exposure: 1/15s</td>
    <td>Exposure: 1/60s</td>
    <td>Exposure: 1/120s</td>
    <td>Exposure: 1/1000s</td>
  </tr>
  <tr>
    <td><img src="imgTest/img-1.jpeg"></td>
    <td><img src="imgTest/img-2.jpeg"></td>
    <td><img src="imgTest/img-3.jpeg"></td>
    <td><img src="imgTest/img-4.jpeg"></td>
    <td><img src="imgTest/img-5.jpeg"></td>
    <td><img src="imgTest/img-6.jpeg"></td>
  </tr>
 </table>
 
 ### Results
 
 <table>
  <tr>
    <td>Debevec's method</td>
    <td>Drago's method</td>
    <td>Mantiuk's method</td>
    <td>Reinhard's method</td>
  </tr>
  <tr>
    <td><img src="imgTest/ldr-Debevec.jpg"></td>
    <td><img src="imgTest/ldr-Drago.jpg"></td>
    <td><img src="imgTest/ldr-Mantiuk.jpg"></td>
    <td><img src="imgTest/ldr-Reinhard.jpg"></td>
  </tr>
    <td>gama=2</td>
    <td>gama=1, saturation=0.7, bias=0.85</td>
    <td>gama=2.2, scale=0.85, saturation=1.2</td>
    <td>gama=1.5, intensity=0, light_adapt=1, color_adapt=0</td>
  </tr>
 </table>
 
# Result in real life

### Imputs
<table>
  <tr>
    <td>Exposure: 1/1000s</td>
    <td>Exposure: 1/30s</td>
    <td>Exposure: 1/8s</td>

  </tr>
  <tr>
    <td><img src="a0.jpg"></td>
    <td><img src="a1.jpg"></td>
    <td><img src="a2.jpg"></td>
  </tr>
   <tr>
    <td><img src="b0.jpg"></td>
    <td><img src="b1.jpg"></td>
    <td><img src="b2.jpg"></td>
  </tr>
    <tr>
    <td><img src="c0.jpg"></td>
    <td><img src="c1.jpg"></td>
    <td><img src="c2.jpg"></td>
  </tr>
 </table>
 
 ### Results
 
 <table>
  <tr>
    <td>Debevec's method</td>
    <td>Drago's method</td>
  </tr>
  <tr>
    <td><img src="ldr-DebevecA.jpg"></td>
    <td><img src="ldr-DragoA.jpg"></td>>
  </tr>
   <tr>
    <td><img src="ldr-DebevecB.jpg"></td>
    <td><img src="ldr-DragoB.jpg"></td>>
  </tr>
    </tr>
   <tr>
    <td><img src="ldr-DebevecC.jpg"></td>
    <td><img src="ldr-DragoC.jpg"></td>>
  </tr>
    <td>gama=4.5</td>
    <td>gama=2, saturation=0.7, bias=0.85</td>
  </tr>
 </table>
