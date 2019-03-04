//
// Name: Aubree Dix
// Date: 3/3/19
// Assignment: HW 6, Variadic stddev
// Class: CS 3560
// File: stddev.cc
//

#include <iostream>
#include <cstdarg>
#include <complex>
#include "stddev.h"

double stddev(int n, ...) {
  double original_mean = 0;
  double new_mean = 0;
  double store_args[n];
  va_list args;
  va_start(args, n);
  for(int j = 0; j < n; ++j) {
    store_args[j] = va_arg(args, int);
    original_mean += store_args[j];
  }
  original_mean = (original_mean / n);
  for(int k = 0; k < n; ++k) {
    store_args[k] = (store_args[k] - original_mean);
    new_mean += (store_args[k] * store_args[k]);
  }
  new_mean = (new_mean / n);
  return sqrt(new_mean);
}
