#include "ecu_state.pb.h"
#include <memory>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
  std::vector<int> spiralOrder(std::vector<std::vector<int>> &matrix) {
    std::vector<int> result;
    return result;
  }
};

int main() {
  demo::ecu_state pb_data;
  
  std::vector<std::vector<int>> myVector = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

  auto sol = std::make_unique<Solution>();
  auto isHappy19 = sol->spiralOrder(myVector);
}