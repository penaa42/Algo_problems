/////////////////////////
///// Algo Practice /////
/////////////////////////

/////////////////////
///// Section 1 /////
/////////////////////

// 1) print all integers from 1 to 255
// for (let i = 0; i <= 255; i++){
//     console.log(i)
// }

// 2) print sum 0-255; with each integer print the sum so far
// let sum = 0;
// for (let i = 0; i <= 255; i++){
//     console.log(`current count is ${i}`)
//     sum = sum + i;
//     console.log(`current sum is ${sum}`)
// }

// 3) find and print max
// let largest_num = 0;
// function arr_max(arr){
//     for (let i = 0; i < arr.length; i++){
//         if (arr[i] > largest_num){
//             largest_num = arr[i];
//         }
//     }
//     console.log(largest_num);
// }
// arr_max([3,5,6,78,1,8]);
// arr_max([1,2,3,4,34,79,31,27]);

// 4) array with odds; array with all odd between 1-255
// let odd_arr = [];
// for (let i = 1; i <= 255; i++){
//     if (i % 2 !== 0){
//         odd_arr.push(i);
//     }
// }
// console.log(odd_arr);

// 5) greater than y
// function greater_than(arr, y){
//     let count = 0;
//     for (let i = 0; i < arr.length; i++){
//         if (arr[i] > y){
//             count = count + 1;
//         }
//     }
//     console.log(count)
// }
// greater_than([1,2,3,4,5,6,7], 5)
// greater_than([1,2,3,4], 5)

// 6) max, min, average; print max, min, and ave for an array
// function arr_max_min_ave(arr){
//     let sum = 0;
//     let ave = 0;
//     let max = 0;
//     for (let i = 0; i < arr.length; i++){
//         if (arr[i] > max){
//             max = arr[i];
//         }
//         sum = sum + arr[i];
//     }
//     for (let i = 0; i < 1; i++){
//         arr.sort();
//     }
//     ave = sum / arr.length;
//     console.log(`Max is ${max}, min is ${arr[0]}, average is ${ave}`)
// }
// arr_max_min_ave([1,2,3,4,5,6,7,8,9])
// arr_max_min_ave([3,1,6,2,7,9,30,25])
// arr_max_min_ave([4,2,8,0,10,15])

// 7) swap string for negative array
// function neg_swap(arr){
//     let new_arr = [];
//     for (let i = 0; i < arr.length; i++){
//         if (arr[i] < 0){
//             new_arr.push(`Dojo`);
//         }
//         else {
//             new_arr.push(arr[i])
//         }
//     }
//     console.log(new_arr)
// }
// neg_swap([2,4,3,7,-1,0,-1,4,-3,-2,-1])

// 8) print odds 1-255
// for (let i = 0; i <= 255; i++){
//     if (i % 2 != 0){
//         console.log(i);
//     }
// }

// 9) iterate and print array
// function arr_iterate(arr){
//     for (let i = 0; i < arr.length; i++){
//         console.log(arr[i]);
//     }
// }
// arr_iterate([1,2,3,4,5,6]);

// 10) get and print average
// function arr_ave(arr){
//     let sum = 0;
//     for (let i = 0; i < arr.length; i++){
//         sum = sum + arr[i];
//     }
//     let average = sum / arr.length;
//     console.log(average);
// }
// arr_ave([1,2,3,4,5,6,7,8,9,10]);

// 11) square the values
// function arr_sqr(arr){
//     let squared_arr = [];
//     for (let i = 0; i < arr.length; i++){
//         squared_arr.push(arr[i] ** 2);
//     }
//     console.log(squared_arr);
// }
// arr_sqr([1,2,3,4,5]);

// 12) zero out nugeative numbers
// function zero_neg(arr){
//     let new_arr = [];
//     for (let i = 0; i < arr.length; i++){
//         if (arr[i] < 0){
//             new_arr.push(0);
//         }
//         else {
//             new_arr.push(arr[i]);
//         }
//     }
//     console.log(new_arr);
// }
// zero_neg([1,-2,3,-1,5,3,-1]);

// 13) shift array values; move all values forward by one index, drop the first and leaving a 0 value at the end
// function arr_shift(arr){
//     let shifted_arr = [];
//     shifted_arr = arr.slice(1);
//     shifted_arr.push(0);
//     console.log(shifted_arr);
// }
// arr_shift([1,2,3,4,5]);
// arr_shift([3,2,6,3,6,3,6,8,4,6,7,3,5,6,3]);

/////////////////////
///// Section 2 /////
/////////////////////

