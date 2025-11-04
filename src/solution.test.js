const test = require('node:test');
const assert = require('node:assert/strict');
const { isValidParentheses } = require('./solution');

test('simple valid', () => {
  assert.equal(isValidParentheses('()[]{}'), true);
});

test('simple invalid', () => {
  assert.equal(isValidParentheses('(]'), false);
});

test('nested valid', () => {
  assert.equal(isValidParentheses('{[()]}'), true);
});
