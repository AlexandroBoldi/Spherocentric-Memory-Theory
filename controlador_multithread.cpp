// Versão paralela do controlador simbólico em C++
#include <webots/Robot.hpp>
#include <thread>
#include <iostream>

void decisao_simbolica() {
  std::cout << "Decisão simbólica paralela executada.\n";
}

int main() {
  webots::Robot robot;
  while (robot.step(32) != -1) {
    std::thread t1(decisao_simbolica);
    t1.join();
  }
  return 0;
}