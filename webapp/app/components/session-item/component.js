import { alias, oneWay, and, notEmpty } from '@ember/object/computed';
import { inject as service } from '@ember/service';
import Component from '@ember/component';

export default Component.extend({
  display: service(),
  tagName: "a",
  attributeBindings: ["href"],
  classNames: ["item", "session", "clickable"],
  classNameBindings: [
    "item.investigated:investigated",
    "is_abandoned:abandoned",
    "result_type",
    "session.computed_status",
    "in_pdb:pdb",
    "interrupted:interrupted",
    "has_any_error:unsuccessful"
  ],

  show_labels: true,

  session: alias("item"),

  href: function() {
    return "/#/sessions/" + this.get("session.display_id");
  }.property("session.id"),

  in_pdb: oneWay("session.in_pdb"),

  interrupted: and(
    "item.finished_running",
    "item.has_tests_left_to_run"
  ),

  has_any_error: function() {
    let item = this.get("item");

    return (
      item.get("num_error_tests") ||
      item.get("num_failed_tests") ||
      item.get("num_errors")
    );
  }.property(
    "item.num_failed_tests",
    "item.num_error_tests",
    "item.num_errors"
  ),

  result_type: oneWay("item.type"),

  abandoned_reason: function() {
    if (this.get("session.is_abandoned")) {
      return "Never completed";
    } else if (
      !this.get("session.num_finished_tests") &&
      this.get("session.end_time")
    ) {
      return "Ended; No finished tests";
    }
  }.property("session.is_abandoned", "session.num_finished_tests"),

  is_abandoned: notEmpty("abandoned_reason"),

  total_num_unsuccessful: function() {
    let item = this.get("item");
    return item.get("num_error_tests") + item.get("num_failed_tests");
  }.property("item.num_error_tests", "item.num_failed_tests")
});
