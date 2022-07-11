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
 

