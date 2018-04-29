import Component from '@ember/component';

export default Component.extend({
  enabled: true,

  actions: {
    toggle: function() {
      this.sendAction();
    }
  }
});
