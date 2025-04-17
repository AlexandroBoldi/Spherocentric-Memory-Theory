// Controlador simbólico básico em C++
#include <webots/Robot.hpp>

int main() {
  webots::Robot robot;
  while (robot.step(32) != -1) {
    // lógica simbólica
  }
  return 0;
}